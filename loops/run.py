from loops.comp_lists_vs_generators_vs_normal_loops import comp


if __name__ == '__main__':
    lists_size = 50000
    print("very small list")
    assert comp(3) > 1
    print("small list")
    assert comp(10) > 10
    print("medium list")
    assert comp(50) > 10
    print("large list")
    assert comp(500) > 10
    print("very large list")
    assert comp(5000) > 10
