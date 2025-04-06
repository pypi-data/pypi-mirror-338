# core/middleware.py

import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp, Receive, Scope, Send
from starlette.datastructures import Headers

logger = logging.getLogger("terminaide")

class ProxyHeaderMiddleware(BaseHTTPMiddleware):
    """
    Middleware that detects and respects common proxy headers for HTTPS, enabling
    terminaide to work correctly behind load balancers and proxies.
    
    This middleware checks multiple headers and indicators to determine if a request
    should be treated as HTTPS, which is critical for preventing mixed-content errors
    when deployed behind proxies, load balancers, or CDNs.
    """
    
    async def dispatch(self, request, call_next):
        # Default to HTTP unless we determine otherwise
        original_scheme = request.scope.get("scheme", "http")
        
        # Get all headers for inspection
        headers = request.headers
        
        # Initialize as not detected
        https_detected = False
        detection_source = None
        
        # Check X-Forwarded-Proto (most common)
        if headers.get("x-forwarded-proto") == "https":
            https_detected = True
            detection_source = "X-Forwarded-Proto"
        
        # Check Forwarded header (RFC 7239)
        elif "forwarded" in headers:
            forwarded = headers.get("forwarded").lower()
            if "proto=https" in forwarded:
                https_detected = True
                detection_source = "Forwarded"
        
        # AWS Elastic Load Balancer sometimes uses this
        elif headers.get("x-forwarded-protocol") == "https":
            https_detected = True
            detection_source = "X-Forwarded-Protocol"
            
        # X-Url-Scheme (used by some proxies)
        elif headers.get("x-url-scheme") == "https":
            https_detected = True
            detection_source = "X-Url-Scheme"
            
        # Front-End-Https (used by some Microsoft proxies)
        elif headers.get("front-end-https") == "on":
            https_detected = True
            detection_source = "Front-End-Https"
            
        # X-ARR-SSL (used by IIS/ARR)
        elif headers.get("x-arr-ssl") is not None:
            https_detected = True
            detection_source = "X-ARR-SSL"
            
        # X-Forwarded-SSL
        elif headers.get("x-forwarded-ssl") == "on":
            https_detected = True
            detection_source = "X-Forwarded-SSL"
        
        # Host-based detection - common cloud platforms usually use HTTPS by default
        host = headers.get("host", "").lower()
        if not https_detected:
            # Check for common cloud hostnames that typically use HTTPS
            cloud_domains = [
                ".amazonaws.com", 
                ".cloudfront.net", 
                ".herokuapp.com", 
                "azurewebsites.net", 
                ".netlify.app"
            ]
            if any(domain in host for domain in cloud_domains) and not host.startswith("localhost"):
                https_detected = True
                detection_source = f"Cloud provider hostname: {host}"
                
        # Check if we're already using HTTPS (scheme already set to https)
        if not https_detected and original_scheme == "https":
            https_detected = True
            detection_source = "Request scope already set to HTTPS"
            
        # Apply the changes if we detected HTTPS
        if https_detected:
            request.scope["scheme"] = "https"
            
            # Only log the first time we see this hostname to avoid log spam
            cache_key = f"https_detected_{host}"
            if not hasattr(self.__class__, cache_key):
                setattr(self.__class__, cache_key, True)
                
                # Log the detection with useful diagnostic information 
                logger.info(
                    f"HTTPS detected via {detection_source} for host '{host}' "
                    f"(original scheme: {original_scheme})"
                )
                
                # Debug log with all headers for troubleshooting  
                if logger.level <= logging.DEBUG:
                    header_dump = ", ".join([f"{k}={v}" for k, v in headers.items()])
                    logger.debug(f"Request headers: {header_dump}")
        
        response = await call_next(request)
        
        # Add security headers to responses when using HTTPS
        if https_detected:
            response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
            
        return response
    
    @staticmethod
    async def set_body(request):
        """Workaround to allow access to request body multiple times."""
        receive = request.receive
        
        async def receive_wrapper():
            nonlocal request
            if not hasattr(request, "_body"):
                request._body = await receive()
            return request._body
            
        request.receive = receive_wrapper
        return request