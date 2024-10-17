import sys
from os.path import join

def generate_config(input_dir, output_conf):
    with open(output_conf, 'w') as config_file:
        with open('header.txt', 'r') as header_file:
            for line in header_file:
                config_file.write(line)

        config_file.write("\n[Rule]\n")
        config_file.write("# from community.lst\n")
        with open(join(input_dir, "community.lst"), "r") as community:
            for line in community:
                config_file.write(f"{"DOMAIN-SUFFIX" if "." in line else "DOMAIN-KEYWORD"},{line.strip()},PROXY\n")

        # ignore since too many
        # config_file.write("# from domains_all.lst\n")
        # with open(join(input_dir, "domains_all.lst"), "r") as domains_all:
        #     for line in domains_all:
        #         config_file.write(f"{"DOMAIN-SUFFIX" if "." in line else "DOMAIN-KEYWORD"},{line.strip()},PROXY\n")

        config_file.write("# from ooni_domains.lst\n")
        with open(join(input_dir, "ooni_domains.lst"), "r") as ooni_domains:
            for line in ooni_domains:
                config_file.write(f"{"DOMAIN-SUFFIX" if "." in line else "DOMAIN-KEYWORD"},{line.strip()},PROXY\n")


        with open(join(input_dir, "user_custom.lst"), "r") as custom:
            for line in custom:
                config_file.write(f"{"DOMAIN-SUFFIX" if "." in line else "DOMAIN-KEYWORD"},{line.strip()},PROXY\n")

        
        with open(join(input_dir, "ipsum.lst"), "r") as ip_networks:
            for line in ip_networks:
                config_file.write(f"IP-CIDR,{line.strip()},PROXY\n")


        config_file.writelines(("\n\n# Финальное правило маршрутизации\n", "FINAL,DIRECT\n"))


if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_conf = sys.argv[2]
    generate_config(input_dir, output_conf)