class Player:
  def __init__(self, name):
      self.name = name

  def play(self):
      print("The player is playing cricket.")

class Batsman(Player):
  def play(self):
      print("The batsman is batting.")

class Bowler(Player):
  def play(self):
      print("The bowler is bowling.")

# Create objects of both the Batsman and Bowler classes
batsman = Batsman("Virat Kohli")
bowler = Bowler("Jasprit Bumrah")

# Call the play() method for each object
batsman.play()
bowler.play()