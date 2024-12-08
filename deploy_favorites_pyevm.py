import boa
# from boa.contracts.vyper.vyper_contract import VyperContract

def main():
    print("Let's read in the Vyper code and deploy it!")
    favorites_contract = boa.load("favorites.vy")
    print(type(favorites_contract))
    
    starting_favorite_number = favorites_contract.retrieve()
    print(f"The starting favorite number is: {starting_favorite_number}")
    
    favorites_contract.store(5)
    ending_favorite_number = favorites_contract.retrieve()
    print(f"The ending favorite number is: {ending_favorite_number}")


if __name__ == "__main__":
    main()