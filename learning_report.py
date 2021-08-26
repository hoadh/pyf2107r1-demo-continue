# Bad:
# f = open('report.csv', 'r')

# # Header
# print(f"{'Họ tên':20s}\tTỉ lệ")
# print(f"{'-' * 20}\t{'-' * 6}")
#
# # Data
# for line in f:
#     if not line.startswith('user_id,name') and line != '\n':
#         # Process
#         values = line.split(",")
#         complete_rate = int(values[5]) / int(values[6]) * 100
#         if complete_rate <= 10:
#             # Output
#             full_name = values[1]
#             print(f"{full_name:20s}\t{complete_rate:.02f}")


# Good
# f = open('report.csv', 'r')
#
# # Header
# print(f"{'Họ tên':20s}\tTỉ lệ")
# print(f"{'-' * 20}\t{'-' * 6}")
#
# # Data
# for line in f:
#     if line.startswith('user_id,name') or line == '\n':
#         continue
#
#     # Process
#     values = line.split(",")
#     complete_rate = int(values[5]) / int(values[6]) * 100
#     if complete_rate > 10:
#         continue
#
#     full_name = values[1]
#     print(f"{full_name:20s}\t{complete_rate:.02f}")
# #

# Better
f = open('report.csv', 'r')

# Header
print(f"{'Họ tên':20s}\tTỉ lệ")
print(f"{'-' * 20}\t{'-' * 6}")

# Data
for line in f:
    not_process = line.startswith('user_id,name') or line == '\n'
    if not_process:
        continue

    # Process
    values = line.split(",")
    complete_rate = int(values[5]) / int(values[6]) * 100
    good_rate = complete_rate > 10

    if good_rate:
        continue

    # Output
    full_name = values[1]
    print(f"{full_name:20s}\t{complete_rate:.02f}")
