from data.cages import Cage
from data.snakes import Snake
from data.owners import Owner


# Updating by document (automatically)
def record_stay(cage_id, snake_id):
    Cage.objects(id=cage_id).update_one(inc__number_of_stays=1)  # Keeps track of people length of stay


# Add snake id to owner
def add_snake(email, name, length, species, is_venomous):

    snake = Snake(name=name, length=length, species=species, is_venomous=is_venomous)
    snake.save()

    num_updated = Owner.objects(email=email).update_one(push__snake_ids=snake.id)

    if num_updated != 1:
        raise Exception("No account with email {}".format(email))

