from typing import List

from bson import ObjectId

from data.bookings import Booking
from data.cages import Cage
from data.owners import Owner


def find_owner_by_email(email: str) -> Owner:
    owner = Owner.objects().filter(email=email).first()
    # filter on 1 or more fields. email must match passed email value
    # Call first to execute the query and return 1 owner or None
    return owner


# Sub-document querying
def get_bookings_for_user(user_id: ObjectId) -> List[Booking]:
    owner = Owner.objects(id=user_id).first()
    booked_cages = Cage \
        .objects(bookings__guest_snake_id__in=owner.snake_ids) \
        .all()

    return list(booked_cages)


# Querying operators
def num_cages_with_sufficient_space(snake_len):
    min_size = snake_len / 4

    # Use __ and operator name without $ to apply for query
    cages = Cage.objects().filter(square_meters__gte=min_size)
    # Count will return the number of matches rather than the documents
    cage_count = Cage.objects(square_meters__gte=min_size).count()

    return cage_count
