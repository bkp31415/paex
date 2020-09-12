# paex
The Parallel Executor - a cloud native distributed process scheduler and executor template

A process distributor, scheduler and executor template that builds on the concepts of distributed computing, with inspiration from the raft algorithm in forming consensus among nodes in a cluster.

We are interested in creating a cheap and efficient system that allows for running compute intensive tasks at scale on the cloud, providing affordable and cloud portable alternative to a single point of failure, expensive infrastructure model prevalent in highly specialised hardware investment models.

The modular nature of the executor allows for varying types of divisible tasks to be run on clusters parallelly with specialised code to handle process division, execution and result retrieval, all of them attachable as modules within paex.
