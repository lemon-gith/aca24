# Advanced Computer Architecture 2024

This repo contains both the coursework reports that I wrote for my 3rd year ACA module, as well as the scripts written to test various parameter configurations.

## CW1 - Energy-Saving Parameter Optimisation

An example [splaytrees test program](have_yet_to_upload_that_file) is run on the architecture configured by us. The performance and power consumption of our solution is simulated using [`SimpleScalar`](https://doi.org/10.1145/268806.268810). We can configure the architecture as we like, e.g. `ruu_size`, `ras_size`, branch predictor types, number of FP ALUs, etc.

The goal was to tune the architecture configurations, to optimise for power savings when running the [`splaytest.c`](same_link_as_above) program, from start to finish.

### Report

This is the primary piece of work produced for this task. My approach was to take an in-depth look at the program and analyse it in relation to its hardware-usage as much as possible, to predict which components, tuned which way, would yield the greatest benefits.

The majority of the [`scripts`](./scripts/) were provided to us, and were altered/modified for use in tuning other parameters. However, as a result of my analysis taking up the majority of my project time, I was rushed for time to carry out the actual simulations, so I had to write a [bash script](#testbashsh) to outsource and parallelise the number-crunching.

In hindsight, an evaluation point for the report is that due to my lack of time to properly review the graphs produced, the 3D graphs that looked great in the interactive plot produced by [`graphing.py`](src/graphing.py), really weren't very legible in 2D format...

### [`testbash.sh`](src/testbash.sh)

This quick test script was only written to help me meet the tight time constraints I'd put myself under, so that I'd be able to run multiple tests in parallel.

To be run on a computer within the Department of Computing network, this script spawns multiple background processes in quick succession, one for each test in `scripts_array`. Each child process will then ssh into a different machine and execute the command line:
- `cd` into the absolute path on the college system, corresponding to this folder: `DIR_PATH`
- run its assigned test script and redirect the resulting output to a file on system
- politely terminate the process running on that guest system

This enabled me to quickly run quite a few tests and `scp` the results back over, to review and produce graphs for my report with.

## CW2 - Paper Review: Ignite

As a trio, we chose an interesting paper from a given list, read through it, and, as is fairly standard, wrote a literature review—albeit with less wider reading, since we were still fairly new to literature reviews back then.

The [uploaded report](./cw2-ignite_review.pdf) is the only file to be uploaded for this coursework. The reference for the reviewed paper is provided, below:

> David Schall, Andreas Sandberg, and Boris Grot. 2023. Warming Up a Cold Front-End with Ignite. In Proceedings of the 56th Annual IEEE/ACM International Symposium on Microarchitecture (MICRO '23). Association for Computing Machinery, New York, NY, USA, 254–267. https://doi.org/10.1145/3613424.3614258
