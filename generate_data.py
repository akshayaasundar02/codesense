from build_dataset import TOPICS_DEF
from generate_data_part1 import PART_1
from generate_data_part2 import PART_2
from generate_data_part3 import PART_3
from generate_data_part4 import PART_4
from generate_data_part5 import PART_5

ALL_QUESTIONS = PART_1 + PART_2 + PART_3 + PART_4 + PART_5

print(f"Total topics: {len(TOPICS_DEF)}")
print(f"Total placement questions aggregated: {len(ALL_QUESTIONS)}")
