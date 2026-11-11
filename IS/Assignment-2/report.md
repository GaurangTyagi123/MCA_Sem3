# Stack Buffer Overflow and Stack Protection

## Objective

The objective of this experiment is to demonstrate a stack-based buffer overflow in a small controlled C program and compare the behavior of an unprotected build with a build using compiler stack-protection mechanisms.

## Vulnerable Program

The program contains a 16-byte local stack buffer:

```c
char buffer[16];
```

It copies the command-line input into the buffer using `strcpy()`:

```c
strcpy(buffer, input);
```

`strcpy()` does not check the destination buffer's size. Therefore, input longer than the available buffer can overwrite adjacent stack data.

## Unprotected Build

The program was compiled with:

```text
gcc -g -O0 -fno-stack-protector vulnerable.c -o vulnerable_unprotected
```

The `-fno-stack-protector` option disables GCC's stack-canary protection. `-g` adds debugging information for GDB and `-O0` keeps optimization disabled, making debugging easier.

### Normal execution

Use:

```text
./vulnerable_unprotected hello
```

Expected behavior:

```text
You entered: hello
Program completed normally.
```

**Insert screenshot here.**

### Oversized input

Use:

```text
./vulnerable_unprotected "$(python3 -c 'print("A"*100)')"
```

On a typical x86-64 Linux build this causes abnormal termination, commonly:

```text
Segmentation fault
```

**Insert screenshot here.**

## GDB Investigation

The unprotected executable was inspected using GDB:

```text
gdb ./vulnerable_unprotected
```

The oversized input was supplied with:

```gdb
run "$(python3 -c 'print("A"*100)')"
```

The call stack was inspected with:

```gdb
bt
```

Registers were inspected with:

```gdb
info registers
```

The stack was inspected with:

```gdb
x/24gx $rsp
```

**Insert GDB screenshot showing the crash and `bt` here.**

**Insert GDB screenshot showing relevant registers/stack here.**

### Interpretation

The local `buffer` occupies only a small region of the stack. Because `strcpy()` copies all input bytes without checking the destination size, the 100-byte input can overwrite data located beyond the buffer.

The exact return address, stack pointer, frame pointer, and memory addresses are machine-dependent. Therefore, the actual GDB output from the experiment should be included rather than hard-coded into this report.

## Protected Build

The same source code was recompiled with stack protection enabled:

```text
gcc -g -O0 -fstack-protector-all vulnerable.c -o vulnerable_protected
```

The same oversized input was then supplied:

```text
./vulnerable_protected "$(python3 -c 'print("A"*100)')"
```

A typical result is:

```text
*** stack smashing detected ***: terminated
Aborted
```

**Insert screenshot here.**

## Explanation of the Protection

With stack protection enabled, the compiler places a stack canary near protected stack data. Before returning from the function, generated code checks whether the canary has been modified.

The oversized input overwrites stack memory and can modify the canary. The check then detects the corruption and terminates the program instead of allowing execution to continue with a corrupted stack frame.

## Comparison

| Build | Compiler option | Normal input | Oversized input |
|---|---|---|---|
| Unprotected | `-fno-stack-protector` | Completes normally | Typically crashes |
| Protected | `-fstack-protector-all` | Completes normally | Detects stack smashing and aborts |

## Conclusion

The experiment demonstrates why unchecked writes to fixed-size stack buffers are dangerous. In the unprotected build, oversized input can corrupt stack data and cause abnormal control flow or a crash. In the protected build, stack-canary checking detects the corruption and terminates the process before the corrupted stack frame can be used normally.
