import os
import ctypes
from ctypes import wintypes

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

ERROR_PARTIAL_COPY = 0x012B
PROCESS_VM_READ = 0x0010

SIZE_T = ctypes.c_size_t
PSIZE_T = ctypes.POINTER(SIZE_T)


def _check_zero(result, func, args):
    if not result:
        raise ctypes.WinError(ctypes.get_last_error())
    return args


kernel32.OpenProcess.errcheck = _check_zero
kernel32.OpenProcess.restype = wintypes.HANDLE
kernel32.OpenProcess.argtypes = (
    wintypes.DWORD,
    wintypes.BOOL,
    wintypes.DWORD)

kernel32.ReadProcessMemory.errcheck = _check_zero
kernel32.ReadProcessMemory.argtypes = (
    wintypes.HANDLE,
    wintypes.LPCVOID,
    wintypes.LPVOID,
    SIZE_T,
    PSIZE_T)

kernel32.CloseHandle.argtypes = (wintypes.HANDLE,)


def read_process_memory(pid, address, size, allow_partial=False):
    buf = (ctypes.c_char * size)()
    nread = SIZE_T()
    hProcess = kernel32.OpenProcess(PROCESS_VM_READ, False, pid)
    try:
        kernel32.ReadProcessMemory(hProcess, address, buf, size, ctypes.byref(nread))
    except WindowsError as e:
        if not allow_partial or e.winerror != ERROR_PARTIAL_COPY:
            raise
    finally:
        kernel32.CloseHandle(hProcess)
    return buf[:nread.value]


def memory_reader(pid, hex_address, size=1024):
    pid = str(pid).strip()
    pid = int(pid)
    hex_address = int(hex_address, base=16)
    value = read_process_memory(pid, hex_address, size)
    return value


def find_mem(mem, start, end):
    _mem = str(mem)
    idx = _mem.find(start)
    _mem = _mem[idx:]
    idx = _mem.find(end)
    _mem = _mem[:idx]
    _mem = _mem.replace(start, '')
    return _mem
