# C++20中的jthread和stop_token

## 前言

C++20中引入了[jthread类](https://en.cppreference.com/w/cpp/thread/jthread)，相关介绍如下：
>The class jthread represents a single thread of execution. It has the same general behavior as std::thread, except that jthread automatically rejoins on destruction, and can be cancelled/stopped in certain situations.
>
>Threads begin execution immediately upon construction of the associated thread object (pending any OS scheduling delays), starting at the top-level function provided as a constructor argument. The return value of the top-level function is ignored and if it terminates by throwing an exception, std::terminate is called. The top-level function may communicate its return value or an exception to the caller via std::promise or by modifying shared variables (which may require synchronization, see std::mutex and std::atomic)
>
>Unlike std::thread, the jthread logically holds an internal private member of type std::stop_source, which maintains a shared stop-state. The jthread constructor accepts a function that takes a std::stop_token as its first argument, which will be passed in by the jthread from its internal stop_source. This allows the function to check if stop has been requested during its execution, and return if it has.
>
>std::jthread objects may also be in the state that does not represent any thread (after default construction, move from, detach, or join), and a thread of execution may be not associated with any jthread objects (after detach).
>
>No two std::jthread objects may represent the same thread of execution; std::jthread is not CopyConstructible or CopyAssignable, although it is MoveConstructible and MoveAssignable.

jthread和thread行为基本一致，可以看做是对thread的包装，jthread可以在销毁时实现自动的join，也就是说无需手动调用join()函数。并且，jthread提供了一套机制，可以实现线程的取消/停止，即本文即将介绍的stop_token（个人感觉和C#的[CancellationToken](https://docs.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken?view=net-5.0)有点相似）。

## 使用

jthread配合stop_token可以实现线程的取消/停止：

```c++
#include <iostream>
#include <thread>
#include <chrono>

using namespace std;

int main(int argc, char *argv[]) {
    auto f = [](const stop_token &st) { // jthread负责传入stop_token
        while (!st.stop_requested()) { // jthread并不会强制停止线程，需要我们依据stop_token的状态来进行取消/停止操作
            cout << "other: " << this_thread::get_id() << "\n";
            this_thread::sleep_for(1s);
        }
        cout << "other thread stopped!\n";
    };
    jthread jth(f);

    cout << "main: " << this_thread::get_id() << "\n";
    this_thread::sleep_for(5s);

    jth.request_stop(); // 请求停止线程，对应的stop_token的stop_requested()函数返回true（注意，除了手动调用外，jthread销毁时也会自动调用该函数）
    // 我们无需在jthread上调用join()，它在销毁时自动join
}
```

输出：

```txt
main: 15116
other: 13776
other: 13776
other: 13776
other: 13776
other: 13776
other thread stopped!
```

参考：
> <https://en.cppreference.com/w/cpp/thread/jthread>
