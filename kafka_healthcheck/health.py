#  Copyright 2019 Shawn Seymour. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License"). You
#  may not use this file except in compliance with the License. A copy of
#  the License is located at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  or in the "license" file accompanying this file. This file is
#  distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
#  ANY KIND, either express or implied. See the License for the specific
#  language governing permissions and limitations under the License.

from __future__ import unicode_literals

import logging
import subprocess


class Health:

    def __init__(self, kafka_host, kafka_port):
        self.kafka_host = kafka_host
        self.kafka_port = kafka_port
        self.log_initialization_values()

    def get_health_result(self):
        try:
            is_healthy = self.is_healthy()
            health_result = {"healthy": is_healthy}
        except Exception as ex:
            logging.error("Error while attempting to calculate health result. Assuming unhealthy. Error: {}".format(ex))
            health_result = {
                "healthy": False,
                "message": "Exception raised while attempting to calculate health result, assuming unhealthy.",
                "error": "{}".format(ex)
            }
        return health_result

    def log_initialization_values(self):
        logging.info("Server will healthcheck against kafka host: {}".format(self.kafka_host))
        logging.info("Server will healthcheck against kafka port: {}".format(self.kafka_port))

    def is_healthy(self):
        process_one = subprocess.Popen(
            ["kcat", "-b", "{}:{}".format(self.kafka_host, self.kafka_port), "-L"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        (output, err) = process_one.communicate()
        exit_code = process_one.wait()
        output = output.decode("utf-8").strip()
        if exit_code == 0:
            logging.debug("kafkacat returned response: {}".format(output))
            is_ok = output.startswith("Metadata for all topics")
            if is_ok:
                logging.debug("kafka Metadata check returned response: {}".format(output))
            else:
                logging.warning("kafka Metadata is not healthy: {}".format(output))
            return is_ok
        else:
            logging.warning("kafka Metadata returned exit code: {}, marking unhealthy...".format(exit_code))
            return False
