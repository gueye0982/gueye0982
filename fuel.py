- 👋 Hi, I’m @gueye0982
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...

<!---
gueye0982/gueye0982 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
def calculateur_carburant(entree):
  numerateur, denominateur = map(int, entree.split('/'))
  pourcentage = (numerateur / denominateur) * 100
  if pourcentage <= 1:
    return 'E'
  elif pourcentage >= 99:
    return 'F'
  else:
    return round(pourcentage)

def main():
  x_y = input("Entrez la fraction de carburant (au format X/Y) : ")
  pourcentage_x_y = calculateur_carburant(x_y)
  if pourcentage_x_y == 'E':
    print("Le réservoir est essentiellement vide.")
  elif pourcentage_x_y == 'F':
    print("Le réservoir est essentiellement plein.")
  else:
    print(f"La quantité de carburant dans le réservoir est d'environ {pourcentage_x_y}%.")

if __name__ == "__main__":
  main()
