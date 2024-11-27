class EVotingSystem:
    def __init__(self):
        self.voters = {}  # Stores voter ID and whether they have voted
        self.candidates = {}  # Stores candidates and their votes

    def register_voter(self, voter_id):
        if voter_id in self.voters:
            print(f"Voter {voter_id} is already registered.")
        else:
            self.voters[voter_id] = False
            print(f"Voter {voter_id} registered successfully.")

    def add_candidate(self, candidate_name):
        if candidate_name in self.candidates:
            print(f"Candidate {candidate_name} is already in the list.")
        else:
            self.candidates[candidate_name] = 0
            print(f"Candidate {candidate_name} added successfully.")

    def cast_vote(self, voter_id, candidate_name):
        if voter_id not in self.voters:
            print(f"Voter {voter_id} is not registered.")
        elif self.voters[voter_id]:
            print(f"Voter {voter_id} has already voted.")
        elif candidate_name not in self.candidates:
            print(f"Candidate {candidate_name} is not available.")
        else:
            self.candidates[candidate_name] += 1
            self.voters[voter_id] = True
            print(f"Voter {voter_id} voted successfully for {candidate_name}.")

    def tally_votes(self):
        print("\nVoting Results:")
        for candidate, votes in self.candidates.items():
            print(f"{candidate}: {votes} votes")

    def run(self):
        while True:
            print("\n1. Register Voter")
            print("2. Add Candidate")
            print("3. Cast Vote")
            print("4. Tally Votes")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                voter_id = input("Enter Voter ID: ")
                self.register_voter(voter_id)
            elif choice == '2':
                candidate_name = input("Enter Candidate Name: ")
                self.add_candidate(candidate_name)
            elif choice == '3':
                voter_id = input("Enter Voter ID: ")
                candidate_name = input("Enter Candidate Name: ")
                self.cast_vote(voter_id, candidate_name)
            elif choice == '4':
                self.tally_votes()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = EVotingSystem()
    system.run()
class EVotingSystem:
    def __init__(self):
        self.voters = {}  # Stores voter ID and whether they have voted
        self.candidates = {}  # Stores candidates and their votes

    def register_voter(self, voter_id):
        if voter_id in self.voters:
            print(f"Voter {voter_id} is already registered.")
        else:
            self.voters[voter_id] = False
            print(f"Voter {voter_id} registered successfully.")

    def add_candidate(self, candidate_name):
        if candidate_name in self.candidates:
            print(f"Candidate {candidate_name} is already in the list.")
        else:
            self.candidates[candidate_name] = 0
            print(f"Candidate {candidate_name} added successfully.")

    def cast_vote(self, voter_id, candidate_name):
        if voter_id not in self.voters:
            print(f"Voter {voter_id} is not registered.")
        elif self.voters[voter_id]:
            print(f"Voter {voter_id} has already voted.")
        elif candidate_name not in self.candidates:
            print(f"Candidate {candidate_name} is not available.")
        else:
            self.candidates[candidate_name] += 1
            self.voters[voter_id] = True
            print(f"Voter {voter_id} voted successfully for {candidate_name}.")

    def tally_votes(self):
        print("\nVoting Results:")
        for candidate, votes in self.candidates.items():
            print(f"{candidate}: {votes} votes")

    def run(self):
        while True:
            print("\n1. Register Voter")
            print("2. Add Candidate")
            print("3. Cast Vote")
            print("4. Tally Votes")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                voter_id = input("Enter Voter ID: ")
                self.register_voter(voter_id)
            elif choice == '2':
                candidate_name = input("Enter Candidate Name: ")
                self.add_candidate(candidate_name)
            elif choice == '3':
                voter_id = input("Enter Voter ID: ")
                candidate_name = input("Enter Candidate Name: ")
                self.cast_vote(voter_id, candidate_name)
            elif choice == '4':
                self.tally_votes()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = EVotingSystem()
    system.run()
print(dir)