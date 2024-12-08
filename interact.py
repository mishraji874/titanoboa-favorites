import boa
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
import os
from eth_account import Account

load_dotenv()

MY_CONTRACT = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512"

def main():
    rpc = os.getenv("RPC_URL")
    print(rpc)
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)
    
    anvil_key = os.getenv("ANVIL_KEY")
    my_account = Account.from_key(anvil_key)
    boa.env.add_account(my_account, force_eoa=True)
    
    favorite_deployer = boa.load_partial("favorites.vy")
    favorites_contract = favorite_deployer.at(MY_CONTRACT)
    
    favorite_number = favorites_contract.retrieve()
    print(f"Favorite number is {favorite_number}")
    
    favorites_contract.store(22)
    favorite_number_updated = favorites_contract.retrieve()
    print(f"Favorite number is now {favorite_number_updated}")

if __name__ == "__main__":
    main()