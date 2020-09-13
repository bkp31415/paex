import grpc
import time
import random

FOLLOWER, CANDIDATE, LEADER = 0, 1, 2

import rule_pb2
import rule_pb2_grpc

class Instance:
    def __init__(self, id):
        self.role = FOLLOWER
        self.voted_for = None
        self.id = id
        self.current_term = 0
        self.commit_index = -1
        self.last_applied = -1
        self.membership_change_in_progress = False


    def update(self):
        """
        Update the instance to a candidate role if follower timed out, else continue
        if timed out as candidate 
        """
        if self.role == FOLLOWER:
            if time.clock() - self.follower_begin > self.follower_timeout:
                self.as_candidate()

        elif self.role == CANDIDATE:
            if time.clock() - self.election_begin > self.election_timeout:
                print(self.id, "election timeout")
                self.begin_election()

        elif role == LEADER:
            self.sync_log()


    def generate_timeout(self):
        """
        Create a timeout
        """
        return random.randrange(150, 300)

    def as_follower(self):
        """
        Sets the instance up for following the leader
        """
        print(self.id, "becomes a follower (term", self.current_time, ")")
        self.role = FOLLOWER
        self.follower_timeout = self.generate_timeout()
        self.follower_begin = time.clock()
        self.voted_for = None


    def start(self):
        self.as_follower()

    def as_candidate(self):
        """
        Sets up the instance as a CANDIDATE for LEADER
        """
        print(self.id, "becomes a candidate (term", self.current_term+1, ")")
        self.role = CANDIDATE
        self.begin_election()


    def begin_election(self):
        """
        Start the processs of election for a LEADER
        """
        self.election_begin = time.clock()
        self.election_timeout = self.generate_timeout()
        self.current_term += 1
        # TODO: complete election logic

    def on_rpc(self):
        """
        When a gRPC call is made onto the instance during election/heartbeat
        """
        if self.role == FOLLOWER:
            self.follower_begin = time.clock()
            # TODO: write logic for maintaining a FOLLOWER instance
        elif self.role == CANDIDATE:
            self.candidate_begin = time.clock()
            # TODO: write logic for maintaining a CANDIDATE instance
        elif self.role == LEADER:
            # TODO: write logic for maintaining a LEADER instance
            pass

    def get_term(self):
        """
        TODO: Set term for vote 
        """
        return -1

    def as_leader(self):
        """
        Set the instance as a LEADER
        """
        print(self.id, "become leader in clusters (term", self.current_term, ") of cluster")
        self.role = LEADER
        self.sync_log()

    def sync_log(self):
        """
        for node in cluster: request append to log
        """
        pass

    def append_entry(self, entry):
        """
        Append an entry into the log
        """
        print(self.current_term, entry)
        self.try_membership_change(entry)

    def get_role(self):
        """
        Returns a String that denotes the role of an instance
        """
        roles = ["follower", "candidate", "leader"]
        try:
            return roles[self.role]
        except:
            return ""

    def try_membership_change(self, entry):
        """
        Tries to change the membership type of an instance
        """
        if len(entry) <= 1:
            return
        elif entry[0] != '{':
            return
        else:
            self.membership_change_in_progress = True
            # TODO: add logic for raft-group instance membership change

    def resolve_membership_change(self):
        self.membership_change_in_progress = False

    def get_from(self, msg):

