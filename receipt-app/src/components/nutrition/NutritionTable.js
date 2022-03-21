import React from "react";
import { useTable } from "react-table";

const NutritionTable = (props) => {
  const columns = React.useMemo(() =>
    Object.keys(props.nutritions).map((nutritionName) => {
      return {
        Header: nutritionName,
        accessor: nutritionName,
      };
    })
  );

  const data = React.useMemo(() => {
    let oneRow = {};
    console.log(props.nutritions);
    for (let nutritionName in props.nutritions) {
      oneRow[nutritionName] = (props.nutritions[nutritionName] * 100).toFixed(
        2
      );
    }
    return [oneRow];
  });

  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    rows,
    prepareRow,
  } = useTable({ columns, data });

  return (
    <table {...getTableProps()} style={{ border: "solid 1px blue" }}>
      <thead>
        {headerGroups.map((headerGroup) => (
          <tr {...headerGroup.getHeaderGroupProps()}>
            {headerGroup.headers.map((column) => (
              <th
                {...column.getHeaderProps()}
                style={{
                  borderBottom: "solid 3px red",
                  background: "aliceblue",
                  color: "black",
                  fontWeight: "bold",
                }}
              >
                {column.render("Header")}
              </th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody {...getTableBodyProps()}>
        {rows.map((row) => {
          prepareRow(row);
          return (
            <tr {...row.getRowProps()}>
              {row.cells.map((cell) => {
                return (
                  <td
                    {...cell.getCellProps()}
                    style={{
                      padding: "10px",
                      border: "solid 1px gray",
                      background: "papayawhip",
                    }}
                  >
                    {cell.render("Cell")}
                  </td>
                );
              })}
            </tr>
          );
        })}
      </tbody>
    </table>
  );
};

export default NutritionTable;
