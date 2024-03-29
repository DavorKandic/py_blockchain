from hash_util import hash_string_256, hash_block

class Verification:

    @staticmethod
    def valid_proof(transactions, last_hash, proof):
        # Create a string with all the hash inputs
        guess = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) + str(proof)).encode()
        # Hash the string
        # IMPORTANT: This is NOT the same hash that will be stored in the previous_hash
        guess_hash = hash_string_256(guess)
        # Only a hash (which is based on the above inputs) which starts with two zeroes will be accepted
        # This condition is of course defined by you. You could also require 10 leading zeroes in hash
        return guess_hash[0:2] == '00'


    @classmethod
    def verify_chain(cls, blockchain):
        """ Verify the current blockchain and return True if it's valid, False otherwise """
        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue
            if block.previous_hash != hash_block(blockchain[index - 1]):
                return False
            if not cls.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                print('Proof of work is invalid!')
                return False
            return True

    @staticmethod
    def verify_transaction(transaction, get_balance):
        """Verify a transaction by checking whether the sender has sufficient coins

        Arguments:
            :transaction: The transaction that should be verified.
        """
        sender_balance = get_balance()
        return sender_balance >= transaction.amount

    @classmethod
    def verify_transactions(cls, open_transactions, get_balance):
        """Verifies all open transactions."""
        return all([cls.verify_transaction(tx, get_balance) for tx in open_transactions])
