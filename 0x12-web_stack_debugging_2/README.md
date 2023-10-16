# Web Stack Debugging:

## Introduction
Debugging is an art form that takes years to master. As a seasoned software engineer, I can tell you that debugging consumes a significant portion of my time. Experience is the best teacher in this realm, as it exposes you to broken code, buggy systems, and all sorts of edge cases and race conditions.

## Non-Exhaustive Guide to Debugging

### School-Specific Tips
If you're struggling with a piece of code or a Bash script that needs to run on the checker, consider simulating the flow in a Docker container. This approach allows you to mimic the distribution specified in the project requirements.
### Test and Verify Your Assumptions
Debugging often starts with a series of questions aimed at isolating the issue. For instance, if your web server isn't serving pages, you might ask:

- Is the web server running?
- What port should it be listening on?
- Is it actually listening on this port?
- Is it listening on the correct server IP?
- Is a firewall enabled?
- Have you checked the logs?

These questions can guide you toward identifying the problem.

### Quick Overview of Machine State
When connecting to a server, it's crucial to get a quick overview of its state. You can do this with five commands:

1. `w` - Shows server uptime, connected users, and load average.
2. `history` - Reveals previously run commands, giving insights into past activities.
3. `top` - Displays what's currently running on the server.
4. `df` - Indicates disk utilization.
5. `netstat` - Shows what ports your server is listening on.

## Debugging at the Machine Level
Debugging often involves verifying assumptions at the machine level. Ask yourself:

- Does the server have free disk space?
- Can the server handle the CPU load?
- Is there available memory?
- Can the server's disks keep up with read/write IO?

If the answer to any of these questions is 'no,' you have three options:

1. Free up resources.
2. Increase machine resources.
3. Distribute resource usage to other machines.

## Network Issues
For network-level debugging, consider the following:

- Are the expected network interfaces and IPs up and running?
- Is the server listening on the expected sockets?
- Can you connect to the desired socket from your location?
- Are the correct firewall rules in place?

## Process Issues
If software isn't behaving as expected, you can look into:

- Whether the software is started.
- If the software process is running.
- Any interesting logs.

## Conclusion
Debugging can be both fun and frustrating. It's a skill that you'll continually refine throughout your career. The more experienced you become, the trickier the bugs you'll tackle. Happy debugging!
