from collections import deque

def stone_pile_game(test_cases):
    results = []
    for N, A in test_cases:
        dq = deque(A)
        
        if len(dq) == 1:
            results.append((1, dq[0]))  
            continue
        
        turn = 1 
        
        while len(dq) > 1:
            if turn == 1:
                dq.append(dq.popleft()) 
                if len(dq) > 1:
                    dq.popleft()  
            else:
                dq.append(dq.popleft()) 
                dq.append(dq.popleft())  
                if len(dq) > 1:
                    dq.popleft()  
            
            turn = 1 - turn  
        
        last_player = 1 - turn  
        
        results.append((last_player, dq[0]))
    
    return results

def main():
    test_cases = []

    T = int(input("Masukkan jumlah test case: "))

    for t in range(T):
        print(f"\nTest case #{t+1}")
        N = int(input("  Masukkan jumlah batu: "))
        angka_batu = input("  Masukkan angka batu (pisahkan dengan spasi): ")

        batu = list(map(int, angka_batu.strip().split()))
        if len(batu) != N:
            print("  Jumlah batu tidak sesuai dengan jumlah angka yang dimasukkan!")
            return

        test_cases.append((N, batu))

    hasil = stone_pile_game(test_cases)

    print("\nHasil Permainan:")
    for i, (pemain, batu) in enumerate(hasil):
        nama = "Aman" if pemain == 1 else "Akshat"
        print(f"  Test case #{i+1}: Pemain terakhir = {nama}, Batu terakhir = {batu}")

main()
