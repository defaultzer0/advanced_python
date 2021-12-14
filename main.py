from CircularBuffer import CircularBuffer

def main():

    buf = CircularBuffer(4)
    
    print("push_front 1")
    buf.push_front(1)
    printBuf(buf)
    
    buf.push_back(2)
    print("push_back 2")
    printBuf(buf)
    
    print("push_back 3")
    buf.push_front(3)
    printBuf(buf)
    
    print("push_back 4")
    buf.push_front(4)
    printBuf(buf)
    
    print("saving buf...")
    save_buffer(buf)
    
    print("loading buf...")
    new_buf = load_buffer()
    
    printBuf(new_buf)

if __name__ == "__main__":
    main()
