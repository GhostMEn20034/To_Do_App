from django.contrib.auth.tokens import PasswordResetTokenGenerator


class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        hash_value = str(user.is_active) + str(user.pk) + str(timestamp)
        print(hash_value)
        return hash_value


email_verification_token = EmailVerificationTokenGenerator()
