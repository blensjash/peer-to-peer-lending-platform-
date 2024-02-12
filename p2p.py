class P2PLendingPlatform:
    def __init__(self):
        self.users = []  # Simulate a user database
        self.loans = []  # Simulate a loans database
        self.offers = []  # Simulate loan offers database
    
    def register_user(self, user_id, user_type):
        """Register a new user as either a borrower or lender."""
        self.users.append({'user_id': user_id, 'user_type': user_type})
        return f"User {user_id} registered as {user_type}"
    
    def submit_loan_request(self, borrower_id, amount, interest_rate, duration):
        """Allow borrowers to submit loan requests."""
        self.loans.append({
            'borrower_id': borrower_id,
            'amount': amount,
            'interest_rate': interest_rate,
            'duration': duration
        })
        return f"Loan request submitted by {borrower_id} for ${amount}"
    
    def submit_loan_offer(self, lender_id, amount, interest_rate, duration):
        """Allow lenders to submit loan offers."""
        self.offers.append({
            'lender_id': lender_id,
            'amount': amount,
            'interest_rate': interest_rate,
            'duration': duration
        })
        return f"Loan offer submitted by {lender_id} for ${amount}"
    
    def match_loans(self):
        """Match loan requests with offers based on criteria."""
        matches = []
        for loan in self.loans:
            # Find the first offer that matches the loan request criteria (simple matching for demonstration)
            for offer in self.offers:
                if offer['amount'] >= loan['amount'] and offer['interest_rate'] <= loan['interest_rate']:
                    matches.append({
                        'borrower_id': loan['borrower_id'],
                        'lender_id': offer['lender_id'],
                        'amount': loan['amount'],
                        'interest_rate': offer['interest_rate'],
                        'duration': loan['duration']
                    })
                    self.offers.remove(offer)  # Assume the offer is consumed
                    break
        return matches

# Instantiate the platform
platform = P2PLendingPlatform()

# Simulate user registration
print(platform.register_user("User1", "Borrower"))
print(platform.register_user("User2", "Lender"))

# Simulate loan request and offer
print(platform.submit_loan_request("User1", 1000, 5, 12))  # Borrower, Amount, Interest Rate (%), Duration (months)
print(platform.submit_loan_offer("User2", 1000, 5, 12))    # Lender, Amount, Interest Rate (%), Duration (months)

# Match loans and print the matches
matches = platform.match_loans()
matches
