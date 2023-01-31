'''
Multithreading
Source : https://www.geeksforgeeks.org/multithreading-python-set-1/
01. What is Thread?
In computing, a process is an instance of a computer program that is being executed.
Any process has 3 basic components:

01 An executable program.
02 The associated data needed by the program (variables, work space, buffers, etc.)
03 The execution context of the program (State of process)

A thread is an entity within a process that can be scheduled for execution.
it is the smallest unit of processing that can be performed in an OS (Operating System). In simple words,
a thread is a sequence of such instructions within a program that can be executed independently of other code.
For simplicity, you can assume that a thread is simply a subset of a process! A thread contains
all this information in a Thread Control Block (TCB):

* Thread Identifier: Unique id (TID) is assigned to every new thread
* Stack pointer: Points to thread’s stack in the process. Stack contains the local variables under thread’s scope.
* Program counter: a register which stores the address of the instruction currently being executed by thread.
* Thread state: can be running, ready, waiting, start or done.
* Thread’s register set: registers assigned to thread for computations.
* Parent process Pointer: A pointer to the Process control block (PCB) of the process that the thread lives on.

Check Image : process_and_thread_relationship.png

Multi-threading: Multiple threads can exist within one process where:
* Each thread contains its own register set and local variables (stored in stack).
* All threads of a process share global variables (stored in heap) and the program code.

Check Image: Single_vs_Multiple_threads.png

         Single Thread process              vs               Multiple thread process
|--------------------------------------|            |--------------------------------------|
| CODE          DATA            FILES  |            | CODE    |      DATA    |      FILES  |
|Register                       Stack  |            | REG     |      REG     |      REG    |
|--------------------------------------|            | STACK   |      STACK   |      STACK  |
|                 \                    |            |--------------------------------------|
|                 /                    |            |   \     |       \      |       \     |
|                 \   <---- THREAD     |            |   /     |       /      |       / <---|----- THREADS
|                 /                    |            |   \     |       \      |       \     |
|                 \                    |            |   /     |       /      |       /     |
|                 /                    |            |   \     |       \      |       \     |
|                 \                    |            |   /     |       /      |       /     |
|--------------------------------------|            |--------------------------------------|

In a simple, single-core CPU, it is achieved using frequent switching between threads.
This is termed as context switching. In context switching, the state of a thread is saved and state of
another thread is loaded whenever any interrupt (due to I/O or manually set) takes place.
Context switching takes place so frequently that all the threads appear to be running parallelly
(this is termed as multitasking).

Check Image : context_switching.png
MultiThread process on single core CPU
|--------------------------------------|    |
|   Thread1         |   Thread2        |    |
|--------------------------------------|    |
|       \           |       \          |    |
|       /           |                  |    |
|       \           |         <--------|----- Thread IDLE waiting for resources (Context switching)
|       /           |       \          |    |
|       \           |       /          |    |
|                   |       \          |    | <--- Time
|                   |       /          |    |
|       \           |       \          |   \/
|--------------------------------------|

'''