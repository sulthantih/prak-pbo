def admin_only(func):
    def wrapper(self, *args, **kwargs):
        if self.admin_mode:
            return func(self, *args, **kwargs)
        else:
            print("You don't have permission to perform this action.")
    return wrapper

class Player:
    def __init__(self, name):
        self.name = name
        self.admin_mode = False

    def __del__(self):
        print(f"Player {self.name} has left the world.")

    def pick_item(self, item):
        print(f"{self.name} picks {item} from the world.")

    def drop_item(self, item):
        print(f"{self.name} drops {item} into the world.")

    def toggle_admin_mode(self):
        self.admin_mode = not self.admin_mode
        if self.admin_mode:
            print(f"{self.name} activates admin mode.")
        else:
            print(f"{self.name} deactivates admin mode.")

class World:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.admin_mode = True

    def __del__(self):
        print(f"The world {self.name} has been destroyed.")

    @admin_only
    def add_item(self, item):
        print(f"An {item} appears in the world.")

    @admin_only
    def remove_item(self, item):
        if item in self.items:
            print(f"The {item} disappears from the world.")
            self.items.remove(item)
        else:
            print(f"The {item} is not in the world.")

def main():
    player_name = input("Enter player name: ")
    player = Player(player_name)
    world = World("Default World")


    player.pick_item("sword")
    player.toggle_admin_mode()
    world.add_item("apple")
    world.remove_item("apple")

if __name__ == "__main__":
    main()
