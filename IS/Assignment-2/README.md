# Stack Buffer Overflow / Stack Protection Lab

This package implements the controlled lab requested in the assignment.

## 1. Compile without stack-protector

```bash
gcc -g -O0 -fno-stack-protector vulnerable.c -o vulnerable_unprotected
```

Test normal input:

```bash
./vulnerable_unprotected hello
```

Test oversized input:

```bash
./vulnerable_unprotected "$(python3 -c 'print("A"*100)')"
```

The unprotected build should normally terminate with a segmentation fault on a typical x86-64 Linux environment.

## 2. Inspect the unprotected crash with GDB

Run:

```bash
gdb ./vulnerable_unprotected
```

Inside GDB:

```gdb
run "$(python3 -c 'print("A"*100)')"
bt
info registers
x/24gx $rsp
```

Capture screenshots showing the crash, `bt`, and relevant register/stack output.

Do not invent the register values in the report: they depend on the machine, compiler, and ASLR.

## 3. Compile with stack protection

```bash
gcc -g -O0 -fstack-protector-all vulnerable.c -o vulnerable_protected
```

Run the same oversized input:

```bash
./vulnerable_protected "$(python3 -c 'print("A"*100)')"
```

A typical result is:

```text
*** stack smashing detected ***: terminated
Aborted
```

The exact diagnostic can vary by Linux distribution and libc.

## 4. What to submit

- `vulnerable.c`
- Screenshot of normal execution
- Screenshot of the unprotected crash
- GDB screenshot showing `bt`
- GDB screenshot showing registers/stack
- Screenshot of the protected build terminating after detecting stack smashing
- The report (`report.md`)

## Important

The GDB register/backtrace output must be captured on your own machine. It should not be fabricated because addresses and register values are environment-dependent.
