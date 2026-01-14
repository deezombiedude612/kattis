N = int(input())
bin_N = str(bin(N))[2:]
# rev_bin_N = bin_N[::-1]
print(sum([int(bin_N[i]) * 2**i for i in range(len(bin_N))]))
