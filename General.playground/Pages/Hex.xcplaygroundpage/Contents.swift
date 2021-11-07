import Foundation

let hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

let output = hex
    .reduce(Array<String>()) { a, b in
        let next = String(b)
        if let previousPair = a.last {
            if previousPair.count == 2 {
                return a + [next]
            } else {
                return a.prefix(a.count - 1) + [previousPair + next]
            }
        } else {
            return [next]
        }
    }
    .compactMap { Int($0, radix: 16) }
    .map(Converter.asciiBinaryToString)

print(output.joined())
