from day_1.task_one import get_sorted_lists_from_input

def main():
    list_1, list_2 = get_sorted_lists_from_input()
    similarity_score = get_similarity_score_from_lists(list_1, list_2)
    print(similarity_score)

def get_similarity_score_from_lists(list_1, list_2):
    cumulative_similarity_score = 0

    for i in range(len(list_1)):
        list_1_id = list_1[i]
        similarity_score = list_1_id * list_2.count(list_1_id)
        cumulative_similarity_score += similarity_score

    return cumulative_similarity_score

if __name__ == '__main__':
    main()