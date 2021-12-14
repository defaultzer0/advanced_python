from CircularBuffer import CircularBuffer

def main():

    buf = CircullarBuffer(4)

    buf.push_front(1)
    buf.push_back(2)
    buf.push_front(3)
    buf.push_front(4)
    printBuf(buf)

    save_buffer(buf)

    new_buf = load_buffer()

    printBuf(new_buf)

if __name__ == "__main__":
    main()
