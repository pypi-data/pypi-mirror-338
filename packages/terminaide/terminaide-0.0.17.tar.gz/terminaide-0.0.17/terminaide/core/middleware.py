# core/middleware.py
from starlette.middleware.base import BaseHTTPMiddleware
import logging

logger = logging.getLogger("terminaide")

class ProxyHeaderMiddleware(BaseHTTPMiddleware):
    """
    Middleware that detects and respects common proxy headers for HTTPS, enabling
    terminaide to work correctly behind load balancers and proxies.
    """
    
    async def dispatch(self, request, call_next):
        # Original scheme before any modifications
        original_scheme = request.scope.get("scheme", "http")
        https_detected = False
        https_source = None
        
        # First check URL scheme itself - if it's already https, respect it
        if original_scheme == "https":
            https_detected = True
            https_source = "URL-Scheme"
        
        # Check X-Forwarded-Proto (most common)
        if not https_detected:
            forwarded_proto = request.headers.get("x-forwarded-proto")
            if forwarded_proto and forwarded_proto.lower() == "https":
                request.scope["scheme"] = "https"
                https_detected = True
                https_source = "X-Forwarded-Proto"
        
        # Check Forwarded header (RFC 7239)
        if not https_detected:
            forwarded = request.headers.get("forwarded")
            if forwarded and "proto=https" in forwarded.lower():
                request.scope["scheme"] = "https"
                https_detected = True
                https_source = "Forwarded"
        
        # AWS ELB sometimes uses this
        if not https_detected:
            elb_proto = request.headers.get("x-forwarded-protocol")
            if elb_proto and elb_proto.lower() == "https":
                request.scope["scheme"] = "https"
                https_detected = True
                https_source = "X-Forwarded-Protocol"
                
        # Cloudflare and some CDNs use this
        if not https_detected:
            cf_visitor = request.headers.get("cf-visitor")
            if cf_visitor and '"scheme":"https"' in cf_visitor.lower():
                request.scope["scheme"] = "https"
                https_detected = True
                https_source = "CF-Visitor"
                
        # X-Scheme is used by some proxies
        if not https_detected:
            x_scheme = request.headers.get("x-scheme")
            if x_scheme and x_scheme.lower() == "https":
                request.scope["scheme"] = "https"
                https_detected = True
                https_source = "X-Scheme"
                
        # Front-End-Https is used by some Microsoft proxies (IIS/ARR)
        if not https_detected:
            front_end_https = request.headers.get("front-end-https")
            if front_end_https and front_end_https.lower() == "on":
                request.scope["scheme"] = "https"
                https_detected = True
                https_source = "Front-End-Https"
                
        # Referer-based detection as last resort
        if not https_detected:
            referer = request.headers.get("referer")
            if referer and referer.lower().startswith("https://"):
                request.scope["scheme"] = "https"
                https_detected = True
                https_source = "Referer"

        # Log when HTTPS is detected but only once per source type
        if https_detected and original_scheme != "https":
            # Safely access app state - handle case where it might not be available
            try:
                app = getattr(request, "app", None)
                if app and hasattr(app, "state"):
                    header_logging_key = f"logged_https_detection_{https_source}"
                    if not hasattr(app.state, header_logging_key):
                        logger.info(
                            f"HTTPS connection detected via {https_source} header "
                            f"(original scheme: {original_scheme})"
                        )
                        # Set flag to avoid spamming logs
                        setattr(app.state, header_logging_key, True)
                else:
                    # Log once per middleware instance if app state is not available
                    logger.info(
                        f"HTTPS connection detected via {https_source} header "
                        f"(original scheme: {original_scheme})"
                    )
            except Exception as e:
                # Failsafe - don't let logging issues break the middleware
                logger.debug(f"Error in middleware logging: {e}")
        
        return await call_next(request)