## 原文

&emsp;摘自Core Java(Volume I--Fundamentals 9th Edition)：

> 1. Name the explicit parameter **otherObject**—later, you will need to cast it to another variable that you should call **other**.
> 2. Test whether **this** happens to be identical to **otherObject**:
`if (this == otherObject) return true;`
This statement is just an optimization. In practice, this is a common case. It is
much cheaper to check for identity than to compare the fields.
> 3. Test whether **otherObject** is null and return false if it is. This test is
required.
`if (otherObject == null) return false;`
> 4. Compare the classes of **this** and **otherObject**. If the semantics of equals
can change in subclasses, use the *getClass* test:
`if (getClass() != otherObject.getClass()) return false;`
If the same semantics holds for all subclasses, you can use an *instanceof* test:
`if (!(otherObject instanceof ClassName)) return false;`
> 5. Cast **otherObject** to a variable of your class type:
`ClassName other = (ClassName) otherObject`
> 6. Now compare the fields, as required by your notion of equality. Use *==* for
primitive type fields, *Objects.equals* for object fields. Return true if all fields
match, false otherwise.
`return field1 == other.field1
&& Objects.equals(field2, other.field2)
&& . . .;`
If you redefine *equals* in a subclass, include a call to `super.equals(other)`.

## 笔记

1. 直接比较是否是同一个引用；
2. 判断需要去比较的对象是否为null；
3. 比较：
equals的语义在子类有所变化，使用getClass；
子类和父类的equals语义一致，使用instanceof；
4. 类型转换；
5. 根据要求进一步比较域。

*关于getClass和instanceof的理解：*
**getClass的规则是：采用==来进行检查是否相等的，是严格的判断，不会存在继承方面的考虑，也就是说只判断该继承层次上是否equals，进一步说子类的equals语义变化了。
instanceof的规则是:你属于该类或者该类的子类吗？考虑了继承，继承层次上equals语义一致；**

> 参考：http://blog.csdn.net/hzw19920329/article/details/51095413
