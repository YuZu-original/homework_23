class DataService:
    @staticmethod
    def filter(lines: list[str], value: str) -> list[str]:
        return list(filter(lambda a: value in a, lines))

    @staticmethod
    def map(lines: list[str], value: str) -> list[str]:
        try:
            value = int(value)
        except ValueError:
            raise ValueError("value must be integer")
        
        result = []
        for line in lines:
            try:
                result.append(line.split()[value])
            except IndexError:
                continue
        return result

    @staticmethod
    def unique(lines: list[str], value: str) -> list[str]:
        return list(set(lines))

    @staticmethod
    def sort(lines: list[str], value: str) -> list[str]:
        reverse = value == "desc"
        return sorted(lines, reverse=reverse)

    @staticmethod
    def limit(lines: list[str], value: str) -> list[str]:
        return lines[:int(value)]

COMMANDS = {
    "filter": DataService.filter,
    "map": DataService.map,
    "unique": DataService.unique,
    "sort": DataService.sort,
    "limit": DataService.limit,
}

def do_command(file_lines: str, cmd: str, val: str):
    func = COMMANDS.get(cmd)
    return func(file_lines, val) if func else file_lines
