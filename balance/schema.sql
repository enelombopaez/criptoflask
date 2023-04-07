DROP TABLE IF EXISTS crypto;

CREATE TABLE crypto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dateoftrans TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    timeoftrans TEXT NOT NULL,
    from_currency TEXT NOT NULL,
    from_quantity REAL,
    to_concurrency TEXT,
    to_quantity REAL
);