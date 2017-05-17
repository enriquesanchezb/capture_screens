#include <Carbon/Carbon.h>

// compile as such:
//  gcc -framework carbon -framework foundation GetWindowList.c

int main(int argc, char **argv) {

    CFArrayRef windowList;

    if (argc != 1) {
        printf("usage: %s\n", argv[0]);
        exit(1);
    }

    windowList = CGWindowListCopyWindowInfo(kCGWindowListExcludeDesktopElements, kCGNullWindowID);
    NSLog(CFSTR("Array: %@"), windowList);
    CFRelease(windowList);

}