class Evaluator:

    def zip_evaluate(coefs, words):
        """zip_evaluate returns sum of length of words wieghted
        by a list of coefficients by using zip()"""
        coefs_len = len(coefs)
        words_len = len(words)
        if (coefs_len != words_len):
            return -1
        sum = 0
        for i,j in zip(words,coefs):
            sum += len(i) * j
        return sum
    pass


    def enumerate_evaluate(coefs, words):
        """enumerate_evaluate returns sum of length of words wieghted
        by a list of coefficients by using enumerate()"""
        coefs_len = len(coefs)
        words_len = len(words)
        if (coefs_len != words_len):
            return -1
        sum = 0
        i = 0
        #Commenting both zip and enumerate
        #for i,(a, b) in enumerate(zip(words, coefs)):
        #     sum += len(a) * b
        for a,b in enumerate(coefs):
                sum += len(words[a]) * b
        return sum
