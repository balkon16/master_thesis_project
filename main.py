# TODO: component for reading investment data
#   * supported formats should include CSV, XLSX, PDF

# TODO: support accounting rules for foreign currencies transactions:
#   * T-1 etc.

# TODO: currencies components:
#   * NBP for tax purposes
#   * other API in order to take into account buy/sell differences
#   * test with mocked API

# TODO: tax component
#   * based on rules (that are legislature dependent) compute tax due, e.g. 19% capital tax gain in Poland
#   * take into account IKE/IKZE rules

# TODO: DB component

# TODO: install Airflow
#  * my DAG must implement a staging area so that failed DAGs can be rerun from a checkpoint

# TODO: DAG deployment:
#   * move DAG
#   * upload Configuration (Variables)

# TODO: alerting
#   * define at least one channel, e.g. mail / Slack

# TODO: type checking - analysis by mypy

# TODO: linter, e.g. black

