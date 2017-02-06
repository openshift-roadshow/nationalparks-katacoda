import mod_wsgi.server

mod_wsgi.server.start(
  '--log-to-terminal',
  '--log-level', 'info',
  '--access-log',
  '--port', '8080',
  '--trust-proxy-header', 'X-Forwarded-For',
  '--trust-proxy-header', 'X-Forwarded-Port',
  '--trust-proxy-header', 'X-Forwarded-Proto',
  '--application-type', 'module',
  '--entry-point', 'wsgi',
  '--inactivity-timeout', '60',
  '--url-alias', '/ws/healthz/', '/opt/app-root/src/LICENSE'
)
