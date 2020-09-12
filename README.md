# paex
The Parallel Executor - a cloud native distributed process scheduler and executor template

A process distributor, scheduler and executor template that builds on the concepts of distributed computing, with inspiration from the raft algorithm in forming consensus among nodes in a cluster.

We are interested in creating a cheap and efficient system that allows for running compute intensive tasks at scale on the cloud, providing affordable and cloud portable alternative to a single point of failure, expensive infrastructure model prevalent in highly specialised hardware investment models.

The modular nature of the executor allows for varying types of divisible tasks to be run on clusters parallelly with specialised code to handle process division, execution and result retrieval, all of them attachable as modules within paex.

##### Visual representation
![paex-refarch](https://user-images.githubusercontent.com/18750864/92993946-a2a30d80-f513-11ea-876e-548d5b9d0a27.png)

#### Use cases
We inted to use paex in creating our implementation of a server farm scale distribution of computational load. The example application in this repo uses divide and conquer approach for image compression, converting the image into an integer matrix and chunking it into small square matrices that can be then sent to the nodes to perform asynchronous processing, the end result recieved from this can then be collated into a final result image.

The front-end application that can be accessed at https://<service node url>:80 will allow for a user to provide the image for processing and will also display the result after processing.
