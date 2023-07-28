# 0x05. Processes and Signals: Learning Objectives

In this project, I have learned the following concepts related to processes and signals:

## General

- **PID (Process ID):** A unique identifier assigned to each process running on a Unix-like operating system. It allows us to interact with processes, monitor their status, and manage them.

- **Process:** A running instance of a program on a computer. It has its own memory space, system resources, and state. Processes are essential for multitasking and executing multiple tasks concurrently.

- **Finding a Process' PID:** I have learned various methods to find the PID of a running process, such as using the `ps` command, `pgrep`, or inspecting process directories under `/proc`.

- **Killing a Process:** Killing a process refers to terminating it prematurely. I have learned to use the `kill` command to send signals to processes, allowing us to terminate them gracefully or forcefully.

- **Signal:** A software interrupt delivered to a process, indicating an event or a request to perform a specific action. Signals can be sent by the operating system, other processes, or the process itself.

- **Two Unignorable Signals:** The two signals that cannot be ignored by a process are `SIGKILL` and `SIGSTOP`. `SIGKILL` immediately terminates the process, while `SIGSTOP` halts its execution temporarily.

By mastering these concepts, I can now effectively manage processes, identify their PIDs, and handle signals to control their behavior. Understanding these fundamentals is crucial for efficient process management in Unix-based systems.