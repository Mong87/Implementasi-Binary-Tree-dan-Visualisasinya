from binary_tree import BinaryTree

tree = BinaryTree()

while True:
    print("\n== Menu Tree ==")
    print("1. Tambah data")
    print("2. Preorder")
    print("3. Inorder")
    print("4. Postorder")
    print("5. Tampilkan Tree (Text)")
    print("6. Tampilkan Tree (Graph/Diagram)")
    print("7. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        data = int(input("Masukkan angka: "))
        tree.insert(data)
    elif pilihan == '2':
        print("Preorder:", end=" ")
        tree.preorder(tree.root)
        print()
    elif pilihan == '3':
        print("Inorder:", end=" ")
        tree.inorder(tree.root)
        print()
    elif pilihan == '4':
        print("Postorder:", end=" ")
        tree.postorder(tree.root)
        print()
    elif pilihan == '5':
        print("\nStruktur tree:")
        tree.display_text(tree.root)
    elif pilihan == '6':
        tree.display_graph()
    elif pilihan == '7':
        print("Keluar dari program")
        break
    else:
        print("⚠️Pilihan tidak valid")