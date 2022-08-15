from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extraindo informações importantes do dataframe


# variáveis para armazenar dados


# método para obter dados do banco de dados


# /api movies


# /api like


# /api dislike


# /api did_not_watch


if __name__ == "__main__":
  app.run()