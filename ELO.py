def update_elo(winner_elo, loser_elo):
    k_factor = 32
    expected_win = 1 / (1 + 10**((loser_elo - winner_elo) / 400))
    updated_winner_elo = winner_elo + k_factor * (1 - expected_win)
    updated_loser_elo = loser_elo - k_factor * (1 - expected_win)
    
    return updated_winner_elo, updated_loser_elo

# Exemple de test
winner_elo = 1500
loser_elo = 1400

updated_winner_elo, updated_loser_elo = update_elo(winner_elo, loser_elo)

print("Ancien Elo du gagnant:", winner_elo)
print("Nouvel Elo du gagnant:", updated_winner_elo)
print("Ancien Elo du perdant:", loser_elo)
print("Nouvel Elo du perdant:", updated_loser_elo)