from data.owners import Owner
import mongoengine

from data.snakes import Snake

owner = Owner(name=name, email=email)
# owner.id is None

owner.save()
# owner.id is objectId('whatever object id is')

snakes = [snake1, snake2]
# ...

Snake.objects().insert(snakes)
