def main():
    f = None
    try:
        f = open('666.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('cant open the file!')
    except LookupError:
        print('unknown code!')
    except UnicodeDecodeError:
        print('UnicodeDecodeError!')
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    main()