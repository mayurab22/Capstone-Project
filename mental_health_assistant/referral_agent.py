"""
ReferralAgent: Refers user to mental health professionals in extreme cases.
"""
class ReferralAgent:
    def refer_professional(self):
        print("[ReferralAgent] Assessing need for professional help...")
        severity = input("Are you experiencing severe distress? (yes/no): ")
        if severity.lower() == 'yes':
            print("It's important to seek professional help. Here are some psychiatrists and counselors in your area:")
            print("1. Dr. Sharma (Psychiatrist)\n2. Dr. Patel (Counselor)\n3. MindCare Clinic")
        else:
            print("If things get overwhelming, don't hesitate to reach out for professional support.")
        # ...additional logic and comments here...
