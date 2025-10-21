// q3b_generic_stack in java

import java.util.ArrayList;

public class GenericStack<T> {
    private ArrayList<T> data = new ArrayList<>();

    public void push(T item) {
        data.add(item);
    }

    public T pop() {
        if (data.isEmpty()) return null;
        return data.remove(data.size() - 1);
    }

    public T top() {
        if (data.isEmpty()) return null;
        return data.get(data.size() - 1);
    }

    public boolean isEmpty() {
        return data.isEmpty();
    }

    public static void main(String[] args) {
        GenericStack<Integer> intStack = new GenericStack<>();
        intStack.push(10);
        intStack.push(20);
        System.out.println("Top integer: " + intStack.top());
        System.out.println("Popped integer: " + intStack.pop());

        GenericStack<String> strStack = new GenericStack<>();
        strStack.push("hello");
        strStack.push("world");
        System.out.println("Top string: " + strStack.top());
        System.out.println("Popped string: " + strStack.pop());
    }
}
