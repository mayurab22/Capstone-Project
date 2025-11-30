"""
Main entry point for the Mental Health Counseling Agent.
This agent provides empathetic support, coping strategies, and referrals to professionals.
"""
from listener_agent import ListenerAgent
from coping_strategy_agent import CopingStrategyAgent
from referral_agent import ReferralAgent

class MentalHealthAssistantAgent:
    def __init__(self):
        self.listener = ListenerAgent()
        self.coping = CopingStrategyAgent()
        self.referral = ReferralAgent()

    def run(self):
        print("Welcome to the Confidential Mental Health Counseling Bot!")
        while True:
            print("\nOptions:")
            print("1. Talk about your feelings")
            print("2. Get coping strategies")
            print("3. Get professional referral")
            print("4. Exit")
            choice = input("Select an option: ")
            if choice == '1':
                self.listener.listen()
            elif choice == '2':
                self.coping.suggest_strategies()
            elif choice == '3':
                self.referral.refer_professional()
            elif choice == '4':
                print("Take care! Remember, your feelings matter.")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    agent = MentalHealthAssistantAgent()
    agent.run()
