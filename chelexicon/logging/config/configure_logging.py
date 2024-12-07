import yaml
import logging
import logging.config
log = logging.getLogger(__name__)

class ConfigureLogging:
    def configure_logging(self):
        # create a log, pull data from logging.conf
        # load the data into a dictionary and run dictConfig
        log = logging.getLogger(__name__)

        def trace(self, message, *args, **kwargs):
            if self.isEnabledFor(5):
                self._log(5, message, args, **kwargs)

        def logToRoot(message, *args, **kwargs):
            logging.log(5, message, args, **kwargs)

        logging.addLevelName(5, 'TRACE')
        setattr(logging, 'TRACE', 5)
        setattr(logging.getLoggerClass(), 'trace', trace)
        setattr(logging, 'trace', logToRoot)

        with open('logging.conf', 'r') as f:
            log_config = yaml.safe_load(f)
        logging.config.dictConfig(log_config)

        return log