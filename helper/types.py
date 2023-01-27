# from logging import basicConfig
# import logging

# logging.basicConfig(
#     level = logging.INFO,
#     filename= 'app.log',
#     filemode= 'a',
#     format= '%(name)s-%(level name)s-%(message)s'
# )

# user = 'mah'
# logging.info(f'user: {user} logged in')
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')