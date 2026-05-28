from datetime import timedelta
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, Int64

paysim_source = FileSource(
    path="data/paysim_features.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp"
)

customer = Entity(name="customer_id", join_keys=["nameOrig"])

customer_stats_view = FeatureView(
    name="customer_transaction_stats",
    entities=[customer],
    ttl=timedelta(days=30),
    schema=[
        Field(name="amount", dtype=Float32),
        Field(name="oldbalanceOrg", dtype=Float32),
        Field(name="newbalanceOrig", dtype=Float32),
        Field(name="transaction_count", dtype=Int64),
    ],
    online=True,
    source=paysim_source,
)