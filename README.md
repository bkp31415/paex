# paex
The Parallel Executor - a cloud native distributed process scheduler and executor

A process distributor, scheduler and executor that builds on the concepts of distributed computing with inspiration from the raft algorithm for the purpose of consensus among nodes in a cluster. We are interested in creating a cheap and efficient system that allows for running highly compute oriented tasks at scale on the cloud for providing affordable and cloud portable alternatives to the single point of failure, expensive infrastructure requirements that come from highly specialized hardware investments. The modular nature of the executor allows for varying types of divisible task to be run on clusters with specialized code to handle process division, execution and result retrieval.
