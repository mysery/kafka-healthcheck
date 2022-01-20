# kafka-healthcheck

A simple healthcheck wrapper to monitor Kafka.

Kafka Healthcheck is a simple server that provides a singular API endpoint to determine the health of a Kafka instance. This can be used to alert or take action on unhealthy Kafka instances.

The service checks the health by sending `kafkacat` about that [kafkacat](https://github.com/edenhill/kafkacat)

This project is a copy "[devshawn](https://github.com/devshawn/zookeeper-healthcheck)" whit modifications for use `kafkacat`

## Usage
Kafka Healthcheck can be installed via `pip`. Both `python` and `pip` are required, as well as `kafkacat`.

### Command-Line
Install `kafka-healthcheck` via `pip`:

```bash
pip install kafka-healthcheck
```

To start the healthcheck server, run:

```bash
kafka-healthcheck
```

The server will now be running on [localhost:9290][localhost].

### Docker solution
Run `kafka-healthcheck` via `dockerhub`:
```bash
docker run -it --network=host -p 9290:9290 \
-e HEALTHCHECK_PORT=9290 \
-e HEALTHCHECK_LOG_LEVEL=DEBUG  \
-e HEALTHCHECK_KAFKA_HOST=localhost \
-e HEALTHCHECK_KAFKA_PORT=9092 \
mysery/kafka-healthcheck:0.0.1 kafka-healthcheck
```
That start docker healtcheck if you have docker in localhost 

## Configuration
Kafka Healthcheck can be configured via command-line arguments or by environment variables.

#### Port
The port for the `kafka-healthcheck` API.

| Usage                 | Value              |
|-----------------------|--------------------|
| Environment Variable  | `HEALTHCHECK_PORT` |
| Command-Line Argument | `--port`           |
| Default Value         | `9290`             |

#### Kafka Host
The host of the Kafka instance to run the health check against. This is used with `kafkacat`.

| Usage                 | Value                    |
|-----------------------|--------------------------|
| Environment Variable  | `HEALTHCHECK_KAFKA_HOST` |
| Command-Line Argument | `--kafka-host`           |
| Default Value         | `localhost`              |

#### Kafka Port
The port of the Kafka instance to run the health check against. This is used with `kafkacat`.

| Usage                 | Value                    |
|-----------------------|--------------------------|
| Environment Variable  | `HEALTHCHECK_KAFKA_PORT` |
| Command-Line Argument | `--kafka-port`           |
| Default Value         | `9092`                   |

#### Log Level
The level of logs to be shown by the application.

| Usage                 | Value                               |
|-----------------------|-------------------------------------|
| Environment Variable  | `HEALTHCHECK_LOG_LEVEL`             |
| Command-Line Argument | `--log-level`                       |
| Default Value         | `INFO`                              |
| Valid Values          | `DEBUG`, `INFO`, `WARNING`, `ERROR` |

All healthy responses are logged at `DEBUG`. Unhealthy responses are logged at `WARNING`. Any unexpected errors are logged at `ERROR`.

## License
Copyright (c) 2019 Shawn Seymour.

Extended Copyright (c) 2022 Rodrigo Garcia.

Licensed under the [Apache 2.0 license][license].

[localhost]: http://localhost:9290
[license]: LICENSE
