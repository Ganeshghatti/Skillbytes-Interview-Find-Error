"""
Seeds the `users` collection with a large, realistic dataset.

Usage:
    python scripts/seed_users.py --count 500000

Run from the backend/ directory with the virtualenv active and a valid
.env (MONGODB_URI / DATABASE_NAME) in place.
"""

import argparse
import os
import random
import sys
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from faker import Faker
from pymongo import MongoClient

load_dotenv()

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BATCH_SIZE = 5000
DEPARTMENTS = ["Engineering", "Sales", "Support", "Marketing", "Operations", "Finance", "HR"]

# Most accounts are regular end users; staff roles are a minority -
# same shape as a real product's user base.
ROLE_WEIGHTS = [
    ("user", 0.90),
    ("manager", 0.04),
    ("teacher", 0.04),
    ("admin", 0.02),
]


def pick_role() -> str:
    roles, weights = zip(*ROLE_WEIGHTS)
    return random.choices(roles, weights=weights, k=1)[0]


def build_user(faker: Faker) -> dict:
    created_at = datetime.now(timezone.utc) - timedelta(days=random.randint(0, 1500))
    return {
        "full_name": faker.name(),
        "email": faker.unique.email(),
        "role": pick_role(),
        "department": random.choice(DEPARTMENTS),
        "phone": faker.phone_number(),
        "is_active": random.random() > 0.05,
        "created_at": created_at.isoformat(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=500_000)
    parser.add_argument("--drop", action="store_true", help="Drop the users collection before seeding")
    args = parser.parse_args()

    mongodb_uri = os.environ["MONGODB_URI"]
    database_name = os.environ.get("DATABASE_NAME", "interview")

    client = MongoClient(mongodb_uri)
    db = client[database_name]
    collection = db["users"]

    if args.drop:
        print("Dropping existing users collection...")
        collection.drop()

    faker = Faker()
    Faker.seed(42)
    random.seed(42)

    inserted = 0
    batch: list[dict] = []

    print(f"Seeding {args.count} users into '{database_name}.users'...")
    for i in range(args.count):
        batch.append(build_user(faker))

        if len(batch) >= BATCH_SIZE:
            collection.insert_many(batch, ordered=False)
            inserted += len(batch)
            batch = []
            print(f"  inserted {inserted}/{args.count}", end="\r")

    if batch:
        collection.insert_many(batch, ordered=False)
        inserted += len(batch)

    print(f"\nDone. Inserted {inserted} users.")
    client.close()


if __name__ == "__main__":
    main()
